"""empty message

Revision ID: 2b8a080e41e8
Revises: 9948bd22d7e2
Create Date: 2023-12-08 09:29:55.745391

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2b8a080e41e8'
down_revision = '9948bd22d7e2'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('assignments',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('role', sa.String(), nullable=True),
    sa.Column('start_date', sa.DateTime(), nullable=True),
    sa.Column('end_date', sa.DateTime(), nullable=True),
    sa.Column('employee_id', sa.Integer(), nullable=True),
    sa.Column('project_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['employee_id'], ['employees.id'], name=op.f('fk_assignments_employee_id_employees')),
    sa.ForeignKeyConstraint(['project_id'], ['projects.id'], name=op.f('fk_assignments_project_id_projects')),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('assignemnts')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('assignemnts',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('role', sa.VARCHAR(), nullable=True),
    sa.Column('start_date', sa.DATETIME(), nullable=True),
    sa.Column('end_date', sa.DATETIME(), nullable=True),
    sa.Column('employee_id', sa.INTEGER(), nullable=True),
    sa.Column('project_id', sa.INTEGER(), nullable=True),
    sa.ForeignKeyConstraint(['employee_id'], ['employees.id'], name='fk_assignemnts_employee_id_employees'),
    sa.ForeignKeyConstraint(['project_id'], ['projects.id'], name='fk_assignemnts_project_id_projects'),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('assignments')
    # ### end Alembic commands ###