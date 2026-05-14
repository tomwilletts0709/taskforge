from sqlalchemy import select
from sqlalchemy.orm import Session

from app.audit.models import Audit


class AuditRepository: 
    def __init__(self, db:Session):
        self.db = db

    def create_audit(self, audit: Audit) -> Audit: 
        self.db.add(audit)
        self.db.commit()
        self.db.refresh(audit)
        return audit
    
    def get_audit(self, audit_id: int) -> Audit:
        statement = select(Audit).where(Audit.id == audit_id)
        result = self.db.execute(statement).scalars().first()

        if result is None: 
            raise ValueError("Cannot Find Audit Details")
        return result
    
    def list_audits(self) -> list[Audit]: 
        statmenent = select(Audit)
        return self.db.execute(statement).scalars().all()
    
    def list_audits_for_project(self, project_id:int) -> list[Audit]: 
        statement = select(Audit).where(Audit.project_id == project_id)
        return self.db.execute(statment).scalars().all()
    




