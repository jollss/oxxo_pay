#!/bin/bash

alembic upgrade head
python manage.py run -h 0.0.0.0