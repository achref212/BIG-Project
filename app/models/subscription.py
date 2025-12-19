from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base

class Plan(Base):
    __tablename__ = "plans"

    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    price_monthly = Column(Integer)
    price_yearly = Column(Integer)
    features_json = Column(String)


class Subscription(Base):
    __tablename__ = "subscriptions"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    plan_id = Column(Integer, ForeignKey("plans.id"))
    status = Column(String(20))
    start_date = Column(Date)
    end_date = Column(Date)

    external_provider = Column(String(50))
    external_subscription_id = Column(String(255))

    user = relationship("User", back_populates="subscriptions")
    plan = relationship("Plan")
