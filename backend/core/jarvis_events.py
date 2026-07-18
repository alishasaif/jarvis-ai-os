from PySide6.QtCore import QObject, Signal


class JarvisEvents(QObject):
    """
    Global J.A.R.V.I.S Event Bus

    Every module communicates through this object.
    """

    # =========================
    # AI EVENTS
    # =========================

    state_changed = Signal(object)

    response_token = Signal(object)

    response_finished = Signal(object)

    ai_request = Signal(object)

    ai_error = Signal(object)

    # =========================
    # VOICE EVENTS
    # =========================

    wake_word_detected = Signal()

    voice_command = Signal(object)

    microphone_started = Signal()

    microphone_stopped = Signal()

    # =========================
    # SYSTEM EVENTS
    # =========================

    system_updated = Signal(dict)

    cpu_changed = Signal(float)

    ram_changed = Signal(float)

    disk_changed = Signal(float)

    network_changed = Signal(bool)

    battery_changed = Signal(int)

    # =========================
    # UI EVENTS
    # =========================

    notification = Signal(object)

    page_changed = Signal(object)

    hud_message = Signal(object)

    # =========================
    # MEMORY EVENTS
    # =========================

    memory_added = Signal(object)

    memory_recalled = Signal(object)

    # =========================
    # AUTOMATION EVENTS
    # =========================

    open_application = Signal(object)

    close_application = Signal(object)

    # =========================
    # ANDROID EVENTS
    # =========================

    android_connected = Signal()

    android_disconnected = Signal()

    # =========================
    # DEBUG EVENTS
    # =========================

    log = Signal(object)

    warning = Signal(object)

    error = Signal(object)


jarvis_events = JarvisEvents()