"""Store constants."""
import datetime
import voluptuous as vol

from homeassistant.const import (
    ATTR_ENTITY_ID,
    CONF_MODE,
    CONF_CODE,
    ATTR_NAME,
)

from homeassistant.components.alarm_control_panel import (
  AlarmControlPanelEntityFeature,
  AlarmControlPanelState
)
from homeassistant.helpers import config_validation as cv

VERSION = "1.10.8"
NAME = "Alarmo"
MANUFACTURER = "@nielsfaber"

DOMAIN = "alarmo"

CUSTOM_COMPONENTS = "custom_components"
INTEGRATION_FOLDER = DOMAIN
PANEL_FOLDER = "frontend"
PANEL_FILENAME = "dist/alarm-panel.js"

PANEL_URL = "/api/panel_custom/alarmo"
PANEL_TITLE = NAME
PANEL_ICON = "mdi:shield-home"
PANEL_NAME = "alarm-panel"

INITIALIZATION_TIME = datetime.timedelta(seconds=60)
SENSOR_ARM_TIME = datetime.timedelta(seconds=5)

STATES = [
    AlarmControlPanelState.ARMED_AWAY,
    AlarmControlPanelState.ARMED_HOME,
    AlarmControlPanelState.ARMED_NIGHT,
    AlarmControlPanelState.ARMED_CUSTOM_BYPASS,
    AlarmControlPanelState.ARMED_VACATION,
    AlarmControlPanelState.DISARMED,
    AlarmControlPanelState.TRIGGERED,
    AlarmControlPanelState.PENDING,
    AlarmControlPanelState.ARMING,
]

ARM_MODES = [
    AlarmControlPanelState.ARMED_AWAY,
    AlarmControlPanelState.ARMED_HOME,
    AlarmControlPanelState.ARMED_NIGHT,
    AlarmControlPanelState.ARMED_CUSTOM_BYPASS,
    AlarmControlPanelState.ARMED_VACATION
]

ARM_MODE_TO_STATE = {
    "away": AlarmControlPanelState.ARMED_AWAY,
    "home": AlarmControlPanelState.ARMED_HOME,
    "night": AlarmControlPanelState.ARMED_NIGHT,
    "custom": AlarmControlPanelState.ARMED_CUSTOM_BYPASS,
    "vacation": AlarmControlPanelState.ARMED_VACATION
}

STATE_TO_ARM_MODE = {
    AlarmControlPanelState.ARMED_AWAY: "away",
    AlarmControlPanelState.ARMED_HOME: "home",
    AlarmControlPanelState.ARMED_NIGHT: "night",
    AlarmControlPanelState.ARMED_CUSTOM_BYPASS: "custom",
    AlarmControlPanelState.ARMED_VACATION: "vacation"
}

COMMAND_ARM_NIGHT = "arm_night"
COMMAND_ARM_AWAY = "arm_away"
COMMAND_ARM_HOME = "arm_home"
COMMAND_ARM_CUSTOM_BYPASS = "arm_custom_bypass"
COMMAND_ARM_VACATION = "arm_vacation"
COMMAND_DISARM = "disarm"

COMMANDS = [
    COMMAND_DISARM,
    COMMAND_ARM_AWAY,
    COMMAND_ARM_NIGHT,
    COMMAND_ARM_HOME,
    COMMAND_ARM_CUSTOM_BYPASS,
    COMMAND_ARM_VACATION
]

EVENT_DISARM = "disarm"
EVENT_LEAVE = "leave"
EVENT_ARM = "arm"
EVENT_ENTRY = "entry"
EVENT_TRIGGER = "trigger"
EVENT_FAILED_TO_ARM = "failed_to_arm"
EVENT_COMMAND_NOT_ALLOWED = "command_not_allowed"
EVENT_INVALID_CODE_PROVIDED = "invalid_code_provided"
EVENT_NO_CODE_PROVIDED = "no_code_provided"
EVENT_TRIGGER_TIME_EXPIRED = "trigger_time_expired"
EVENT_READY_TO_ARM_MODES_CHANGED = "ready_to_arm_modes_changed"

ATTR_MODES = "modes"
ATTR_ARM_MODE = "arm_mode"
ATTR_CODE_DISARM_REQUIRED = "code_disarm_required"
ATTR_CODE_MODE_CHANGE_REQUIRED = "code_mode_change_required"
ATTR_REMOVE = "remove"
ATTR_OLD_CODE = "old_code"

ATTR_TRIGGER_TIME = "trigger_time"
ATTR_EXIT_TIME = "exit_time"
ATTR_ENTRY_TIME = "entry_time"

ATTR_ENABLED = "enabled"
ATTR_USER_ID = "user_id"

ATTR_CAN_ARM = "can_arm"
ATTR_CAN_DISARM = "can_disarm"
ATTR_DISARM_AFTER_TRIGGER = "disarm_after_trigger"
ATTR_IGNORE_BLOCKING_SENSORS_AFTER_TRIGGER = "ignore_blocking_sensors_after_trigger"

ATTR_REMOVE = "remove"
ATTR_IS_OVERRIDE_CODE = "is_override_code"
ATTR_AREA_LIMIT = "area_limit"
ATTR_CODE_FORMAT = "code_format"
ATTR_CODE_LENGTH = "code_length"

ATTR_AUTOMATION_ID = "automation_id"

ATTR_TYPE = "type"
ATTR_AREA = "area"
ATTR_MASTER = "master"

ATTR_TRIGGERS = "triggers"
ATTR_ACTIONS = "actions"
ATTR_EVENT = "event"
ATTR_REQUIRE_CODE = "require_code"

ATTR_NOTIFICATION = "notification"
ATTR_VERSION = "version"
ATTR_STATE_PAYLOAD = "state_payload"
ATTR_COMMAND_PAYLOAD = "command_payload"

ATTR_FORCE = "force"
ATTR_SKIP_DELAY = "skip_delay"
ATTR_CONTEXT_ID = "context_id"

PUSH_EVENT = "mobile_app_notification_action"

EVENT_ACTION_FORCE_ARM = "ALARMO_FORCE_ARM"
EVENT_ACTION_RETRY_ARM = "ALARMO_RETRY_ARM"
EVENT_ACTION_DISARM = "ALARMO_DISARM"
EVENT_ACTION_ARM_AWAY = "ALARMO_ARM_AWAY"
EVENT_ACTION_ARM_HOME = "ALARMO_ARM_HOME"
EVENT_ACTION_ARM_NIGHT = "ALARMO_ARM_NIGHT"
EVENT_ACTION_ARM_VACATION = "ALARMO_ARM_VACATION"
EVENT_ACTION_ARM_CUSTOM_BYPASS = "ALARMO_ARM_CUSTOM_BYPASS"

EVENT_ACTIONS = [
    EVENT_ACTION_FORCE_ARM,
    EVENT_ACTION_RETRY_ARM,
    EVENT_ACTION_DISARM,
    EVENT_ACTION_ARM_AWAY,
    EVENT_ACTION_ARM_HOME,
    EVENT_ACTION_ARM_NIGHT,
    EVENT_ACTION_ARM_VACATION,
    EVENT_ACTION_ARM_CUSTOM_BYPASS
]

MODES_TO_SUPPORTED_FEATURES = {
    AlarmControlPanelState.ARMED_AWAY: AlarmControlPanelEntityFeature.ARM_AWAY,
    AlarmControlPanelState.ARMED_HOME: AlarmControlPanelEntityFeature.ARM_HOME,
    AlarmControlPanelState.ARMED_NIGHT: AlarmControlPanelEntityFeature.ARM_NIGHT,
    AlarmControlPanelState.ARMED_CUSTOM_BYPASS: AlarmControlPanelEntityFeature.ARM_CUSTOM_BYPASS,
    AlarmControlPanelState.ARMED_VACATION: AlarmControlPanelEntityFeature.ARM_VACATION
}

SERVICE_ARM = "arm"
SERVICE_DISARM = "disarm"
SERVICE_SKIP_DELAY = "skip_delay"

CONF_ALARM_ARMED_AWAY = "armed_away"
CONF_ALARM_ARMED_CUSTOM_BYPASS = "armed_custom_bypass"
CONF_ALARM_ARMED_HOME = "armed_home"
CONF_ALARM_ARMED_NIGHT = "armed_night"
CONF_ALARM_ARMED_VACATION = "armed_vacation"
CONF_ALARM_ARMING = "arming"
CONF_ALARM_DISARMED = "disarmed"
CONF_ALARM_PENDING = "pending"
CONF_ALARM_TRIGGERED = "triggered"

SERVICE_ARM_SCHEMA = cv.make_entity_service_schema(
    {
        vol.Required(ATTR_ENTITY_ID): cv.entity_id,
        vol.Optional(CONF_CODE, default=""): cv.string,
        vol.Optional(CONF_MODE, default=AlarmControlPanelState.ARMED_AWAY): vol.In([
            "away",
            "home",
            "night",
            "custom",
            "vacation",
            CONF_ALARM_ARMED_AWAY,
            CONF_ALARM_ARMED_HOME,
            CONF_ALARM_ARMED_NIGHT,
            CONF_ALARM_ARMED_CUSTOM_BYPASS,
            CONF_ALARM_ARMED_VACATION,
        ]),
        vol.Optional(ATTR_SKIP_DELAY, default=False): cv.boolean,
        vol.Optional(ATTR_FORCE, default=False): cv.boolean,
        vol.Optional(ATTR_CONTEXT_ID): int
    }
)

SERVICE_DISARM_SCHEMA = cv.make_entity_service_schema(
    {
        vol.Required(ATTR_ENTITY_ID): cv.entity_id,
        vol.Optional(CONF_CODE, default=""): cv.string,
        vol.Optional(ATTR_CONTEXT_ID): int
    }
)

SERVICE_SKIP_DELAY_SCHEMA = cv.make_entity_service_schema(
    {
        vol.Required(ATTR_ENTITY_ID): cv.entity_id,
    }
)

SERVICE_ENABLE_USER = "enable_user"
SERVICE_DISABLE_USER = "disable_user"
SERVICE_TOGGLE_USER_SCHEMA = vol.Schema(
    {
        vol.Required(ATTR_NAME, default=""): cv.string,
    }
)
