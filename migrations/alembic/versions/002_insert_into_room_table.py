from alembic import op
import sqlalchemy as sa
import uuid


revision = '002'
down_revision = '001'

def upgrade():
    op.execute(
        sa.text(
            """
            INSERT INTO room (id, number, available)
            VALUES
                (:id1, 101, TRUE),
                (:id2, 102, FALSE),
                (:id3, 103, TRUE)
            """
        ).bindparams(
            id1=uuid.UUID('a0eebc99-9c0b-4ef8-bb6d-6bb9bd380a11').bytes,
            id2=uuid.UUID('b0eebc99-9c0b-4ef8-bb6d-6bb9bd380a12').bytes,
            id3=uuid.UUID('c0eebc99-9c0b-4ef8-bb6d-6bb9bd380a13').bytes
        )
    )

def downgrade():
    op.execute(
        sa.text(
            """
            DELETE FROM room
            WHERE id IN (
                :id1,
                :id2,
                :id3
            )
            """
        ).bindparams(
            id1=uuid.UUID('a0eebc99-9c0b-4ef8-bb6d-6bb9bd380a11').bytes,
            id2=uuid.UUID('b0eebc99-9c0b-4ef8-bb6d-6bb9bd380a12').bytes,
            id3=uuid.UUID('c0eebc99-9c0b-4ef8-bb6d-6bb9bd380a13').bytes
        )
    )
