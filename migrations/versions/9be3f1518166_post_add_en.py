"""post_add_en

Revision ID: 9be3f1518166
Revises: beb28a5c883a
Create Date: 2020-07-06 01:50:41.378823

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9be3f1518166'
down_revision = 'beb28a5c883a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('post', sa.Column('is_en', sa.Boolean(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('post', 'is_en')
    # ### end Alembic commands ###
