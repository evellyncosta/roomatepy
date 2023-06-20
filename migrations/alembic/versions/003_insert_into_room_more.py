from alembic import op
import sqlalchemy as sa
import uuid

revision = '003'
down_revision = '002'

def upgrade():
    connection = op.get_bind()

    rows = [
        {
            'id': uuid.uuid4().bytes,
            'number': 104,
            'available': True
        },
        {
            'id': uuid.uuid4().bytes,
            'number': 105,
            'available': False
        },
        {
            'id': uuid.uuid4().bytes,
            'number': 106,
            'available': True
        },
        {
            'id': uuid.uuid4().bytes,
            'number': 107,
            'available': False
        },
        {
            'id': uuid.uuid4().bytes,
            'number': 108,
            'available': True
        },
        {
            'id': uuid.uuid4().bytes,
            'number': 109,
            'available': False
        },
        {
            'id': uuid.uuid4().bytes,
            'number': 110,
            'available': True
        },
        {
            'id': uuid.uuid4().bytes,
            'number': 111,
            'available': False
        },
        {
            'id': uuid.uuid4().bytes,
            'number': 112,
            'available': True
        },
        {
            'id': uuid.uuid4().bytes,
            'number': 113,
            'available': False
        },
        {
            'id': uuid.uuid4().bytes,
            'number': 114,
            'available': True
        },
        {
            'id': uuid.uuid4().bytes,
            'number': 115,
            'available': False
        },
        {
            'id': uuid.uuid4().bytes,
            'number': 116,
            'available': True
        },
        {
            'id': uuid.uuid4().bytes,
            'number': 117,
            'available': False
        },
        {
            'id': uuid.uuid4().bytes,
            'number': 118,
            'available': True
        },
        {
            'id': uuid.uuid4().bytes,
            'number': 119,
            'available': False
        },
        {
            'id': uuid.uuid4().bytes,
            'number': 120,
            'available': True
        },
        {
            'id': uuid.uuid4().bytes,
            'number': 121,
            'available': False
        },
        {
            'id': uuid.uuid4().bytes,
            'number': 122,
            'available': True
        },
        {
            'id': uuid.uuid4().bytes,
            'number': 123,
            'available': False
        },
        {
            'id': uuid.uuid4().bytes,
            'number': 124,
            'available': True
        },
        {
            'id': uuid.uuid4().bytes,
            'number': 125,
            'available': False
        },
        {
            'id': uuid.uuid4().bytes,
            'number': 126,
            'available': True
        },
        {
            'id': uuid.uuid4().bytes,
            'number': 127,
            'available': False
        },
        {
            'id': uuid.uuid4().bytes,
            'number': 128,
            'available': True
        },
        {
            'id': uuid.uuid4().bytes,
            'number': 129,
            'available': False
        },
        {
            'id': uuid.uuid4().bytes,
            'number': 130,
            'available': True
        },
        {
            'id': uuid.uuid4().bytes,
            'number': 131,
            'available': False
        },
        {
            'id': uuid.uuid4().bytes,
            'number': 132,
            'available': True
        },
        {
            'id': uuid.uuid4().bytes,
            'number': 133,
            'available': False
        },
    ]

    for row in rows:
        connection.execute(
            sa.text(
                """
                INSERT INTO room (id, number, available)
                VALUES (:id, :number, :available)
                """
            ),
            row
        )

def downgrade():
    op.execute(
        sa.text(
            """
            DELETE FROM room
            WHERE id IN (
                SELECT id
                FROM room
                ORDER BY id DESC
                LIMIT 30
            )
            """
        )
    )
