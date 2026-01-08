"""
Logging Utilities for Jarvis Cluster Management System

This module provides utilities for structured logging with correlation IDs,
sensitive data filtering, and context management.

Example Usage:
    from logging_utils import get_logger, set_correlation_id

    logger = get_logger(__name__)
    set_correlation_id()  # Generate new correlation ID

    logger.info("Task scheduled", extra={"task_id": "task-123", "node_id": "node-1"})
"""

import logging
import logging.config
import os
import re
import uuid
from contextvars import ContextVar
from pathlib import Path
from typing import Any, Dict, Optional

import yaml


# Context variable for correlation ID
correlation_id_var: ContextVar[Optional[str]] = ContextVar("correlation_id", default=None)


def load_logging_config(config_file: Optional[str] = None, environment: Optional[str] = None):
    """
    Load logging configuration from YAML file.

    Args:
        config_file: Path to config file. If None, uses environment-based default.
        environment: Environment name (development, production). Overrides config_file.

    Example:
        # Load development config
        load_logging_config(environment="development")

        # Load specific config file
        load_logging_config(config_file="config/logging/custom.yaml")
    """
    if environment:
        config_file = f"config/logging/{environment}.yaml"
    elif not config_file:
        # Default to standard config
        config_file = "config/logging/logging_config.yaml"

    config_path = Path(config_file)
    if not config_path.exists():
        logging.basicConfig(level=logging.INFO)
        logging.warning(f"Logging config not found: {config_file}, using basicConfig")
        return

    with open(config_path) as f:
        config = yaml.safe_load(f)
        logging.config.dictConfig(config)


def get_logger(name: str) -> logging.Logger:
    """
    Get a logger instance with the given name.

    Args:
        name: Logger name, typically __name__ of the calling module

    Returns:
        Logger instance

    Example:
        logger = get_logger(__name__)
        logger.info("Starting application")
    """
    return logging.getLogger(name)


def set_correlation_id(cid: Optional[str] = None) -> str:
    """
    Set correlation ID for the current context.

    Args:
        cid: Correlation ID to set. If None, generates a new UUID.

    Returns:
        The correlation ID that was set

    Example:
        # Generate new correlation ID
        cid = set_correlation_id()

        # Use existing correlation ID from request
        set_correlation_id(request.headers.get("X-Correlation-ID"))
    """
    if cid is None:
        cid = str(uuid.uuid4())
    correlation_id_var.set(cid)
    return cid


def get_correlation_id() -> Optional[str]:
    """
    Get correlation ID from current context.

    Returns:
        Correlation ID or None if not set

    Example:
        cid = get_correlation_id()
        if cid:
            logger.info("Processing request", extra={"correlation_id": cid})
    """
    return correlation_id_var.get()


def clear_correlation_id():
    """
    Clear correlation ID from current context.

    Example:
        clear_correlation_id()
    """
    correlation_id_var.set(None)


class CorrelationIdFilter(logging.Filter):
    """
    Logging filter that adds correlation ID to log records.

    This filter automatically adds the correlation ID from the current
    context to all log records.

    Example in logging config:
        filters:
          correlation_id:
            (): jarvis.logging.CorrelationIdFilter
    """

    def filter(self, record: logging.LogRecord) -> bool:
        """Add correlation ID to log record."""
        cid = get_correlation_id()
        record.correlation_id = cid if cid else "N/A"
        return True


class SensitiveDataFilter(logging.Filter):
    """
    Logging filter that masks sensitive data in log messages.

    Masks passwords, tokens, API keys, and other sensitive patterns.

    Example in logging config:
        filters:
          sensitive_data:
            (): jarvis.logging.SensitiveDataFilter
    """

    # Patterns to mask
    PATTERNS = [
        (re.compile(r"password['\"]?\s*[:=]\s*['\"]?([^'\"&\s]+)", re.IGNORECASE), "password=***"),
        (re.compile(r"token['\"]?\s*[:=]\s*['\"]?([^'\"&\s]+)", re.IGNORECASE), "token=***"),
        (re.compile(r"api[_-]?key['\"]?\s*[:=]\s*['\"]?([^'\"&\s]+)", re.IGNORECASE), "api_key=***"),
        (re.compile(r"secret['\"]?\s*[:=]\s*['\"]?([^'\"&\s]+)", re.IGNORECASE), "secret=***"),
        (re.compile(r"authorization['\"]?\s*[:=]\s*['\"]?([^'\"&\s]+)", re.IGNORECASE), "authorization=***"),
    ]

    def filter(self, record: logging.LogRecord) -> bool:
        """Mask sensitive data in log message."""
        if isinstance(record.msg, str):
            for pattern, replacement in self.PATTERNS:
                record.msg = pattern.sub(replacement, record.msg)
        return True


class StructuredLogger:
    """
    Wrapper for structured logging with consistent extra fields.

    Example:
        logger = StructuredLogger("jarvis.scheduler")
        logger.info("Task scheduled", task_id="task-123", node_id="node-1")
    """

    def __init__(self, name: str):
        """Initialize structured logger."""
        self.logger = get_logger(name)

    def _log(self, level: int, msg: str, **kwargs):
        """Internal method to log with structured context."""
        extra = {k: v for k, v in kwargs.items() if k not in ["exc_info", "stack_info"]}

        # Add correlation ID if available
        cid = get_correlation_id()
        if cid:
            extra["correlation_id"] = cid

        self.logger.log(
            level,
            msg,
            extra=extra,
            exc_info=kwargs.get("exc_info"),
            stack_info=kwargs.get("stack_info"),
        )

    def debug(self, msg: str, **kwargs):
        """Log debug message with structured context."""
        self._log(logging.DEBUG, msg, **kwargs)

    def info(self, msg: str, **kwargs):
        """Log info message with structured context."""
        self._log(logging.INFO, msg, **kwargs)

    def warning(self, msg: str, **kwargs):
        """Log warning message with structured context."""
        self._log(logging.WARNING, msg, **kwargs)

    def error(self, msg: str, **kwargs):
        """Log error message with structured context."""
        self._log(logging.ERROR, msg, **kwargs)

    def critical(self, msg: str, **kwargs):
        """Log critical message with structured context."""
        self._log(logging.CRITICAL, msg, **kwargs)


def create_audit_logger(name: str = "jarvis.audit") -> logging.Logger:
    """
    Create a logger for audit trails.

    Audit logs should track:
    - User actions
    - Security events
    - Configuration changes
    - Data access

    Args:
        name: Logger name for audit trail

    Returns:
        Logger instance configured for audit logging

    Example:
        audit = create_audit_logger()
        audit.info("User login", user_id="user-123", ip_address="192.168.1.1")
    """
    return get_logger(name)


def log_function_call(logger: logging.Logger):
    """
    Decorator to log function entry and exit.

    Args:
        logger: Logger instance to use

    Example:
        @log_function_call(logger)
        def process_task(task_id: str):
            # Function implementation
            pass
    """

    def decorator(func):
        def wrapper(*args, **kwargs):
            logger.debug(
                f"Entering {func.__name__}",
                extra={"function": func.__name__, "args": args, "kwargs": kwargs},
            )
            try:
                result = func(*args, **kwargs)
                logger.debug(
                    f"Exiting {func.__name__}",
                    extra={"function": func.__name__, "result": result},
                )
                return result
            except Exception as e:
                logger.error(
                    f"Exception in {func.__name__}",
                    exc_info=True,
                    extra={"function": func.__name__, "error": str(e)},
                )
                raise

        return wrapper

    return decorator
