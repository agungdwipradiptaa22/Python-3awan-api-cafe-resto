from sqlalchemy import Column, Integer, String, Numeric, ForeignKey, DateTime, func
from config.database import Base
from sqlalchemy.orm import relationship

class Transaction(Base):
    __tablename__ = "transactions"

    id = Column(Integer, primary_key=True, index=True)
    menu_id = Column(Integer, ForeignKey("menus.id"), nullable=False)
    quantity = Column(Integer, nullable=False)
    total_price = Column(Numeric(10, 2), nullable=False)
    payment_method = Column(String(50), nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    # Relationship
    menu = relationship("Menu")

    def to_dict(self):
        return {
            "id": self.id,
            "menu_id": self.menu_id,
            "quantity": self.quantity,
            "total_price": float(self.total_price),
            "payment_method": self.payment_method,
            "created_at": self.created_at.isoformat() if self.created_at else None,
            "menu": self.menu.to_dict() if self.menu else None
        }
