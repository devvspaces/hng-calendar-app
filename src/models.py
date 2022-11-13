from datetime import datetime

from sqlalchemy import (BigInteger, Boolean, Column, DateTime, ForeignKey,
                        Integer, String)
from sqlalchemy.orm import relationship

from database import Base


class User(Base):
    """
    User model
    """
    __tablename__ = "users"

    id = Column(BigInteger, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    first_name = Column(String)
    last_name = Column(String)
    password = Column(String)
    profile_photo_url = Column(String)

    events = relationship("Event", back_populates="owner")


class Event(Base):
    """
    Event model
    """
    __tablename__ = "events"

    id = Column(BigInteger, primary_key=True, index=True)
    user_id = Column(BigInteger, ForeignKey("users.id"), nullable=False)
    title = Column(String)
    description = Column(String)
    location = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(
        DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    sheduled_at = Column(DateTime, nullable=True)

    user = relationship("User", back_populates="events")


class PollSetting(Base):
    """
    Poll settings for an event
    """
    __tablename__ = "poll_settings"

    id = Column(BigInteger, primary_key=True, index=True)
    event_id = Column(BigInteger, ForeignKey("events.id"), nullable=False)
    active = Column(Boolean, default=True)
    voting_time_frame = Column(DateTime)
    url = Column(String, unique=True, index=True)

    event = relationship("Event", back_populates="poll_setting")


class PollOption(Base):
    """
    Poll options are the options that the voter can choose from
    """
    __tablename__ = "poll_options"

    id = Column(BigInteger, primary_key=True, index=True)
    poll_setting_id = Column(
        BigInteger, ForeignKey("poll_settings.id"), nullable=False)
    count = Column(Integer, default=0)
    date = Column(DateTime)

    poll_setting = relationship("PollSetting", back_populates="poll_options")


class Vote(Base):
    """
    Vote is the actual vote that the voter makes
    """
    __tablename__ = "votes"

    id = Column(BigInteger, primary_key=True, index=True)
    poll_option_id = Column(
        BigInteger, ForeignKey("poll_options.id"), nullable=False)
    full_name = Column(String)
    email = Column(String)

    poll_option = relationship("PollOption", back_populates="votes")
