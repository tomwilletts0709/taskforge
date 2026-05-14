from dataclasses import dataclass

from app.domain import EntityType
from app.audit.repository import AuditRepository
from app.audit.models import Audit

@dataclass
class AuditEvent: 
    actor_user_id: int
    action: str
    entity_type: EntityType
    entity_id: int
    project_id: int | None = None


class AuditService: 
    def __init__(self, audit_repo=AuditRepository): 
        self.audit_repo = audit_repo


    def record_event(self, event: AuditEvent):
     audit = Audit(
        actor_user_id=event.actor_user_id,
        action=event.action,
        entity_type=event.entity_type.value,
        entity_id=event.entity_id,
        project_id=event.project_id,
    )
     return self.audit_repo.create_audit(audit)

    def get_audit(self, audit_id: int) -> Audit: 
        return self.audit_repo.get_audit(audit_id)
    
    def list_audits(self) -> list[Audit]: 
        return self.audit_repo.list_audits()
    
    def list_audits_for_project(self, project_id:id) -> list[Audit]: 
        return self.audit_repo.list_audits_for_project(project_id)
    


