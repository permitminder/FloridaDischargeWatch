"""
State configuration for this FloridaDischargeWatch instance.

All state-specific values are centralized here. To deploy for a new state,
run: python deploy_new_state.py <STATE_CODE>

This file is overwritten by deploy_new_state.py — do not add logic here.
"""

STATE_CODE = "FL"
STATE_NAME = "Florida"
APP_NAME = "FloridaDischargeWatch"
APP_TAGLINE = "Florida Discharge Monitoring"
DOMAIN = "floridadischargewatch.org"
DATA_FILE = "fl_exceedances_launch_ready.csv"
CONTACT_EMAIL = "data@floridadischargewatch.org"
MAILING_ADDRESS = ""
TIMEZONE_LABEL = "EST"
EPA_REGION = 4
