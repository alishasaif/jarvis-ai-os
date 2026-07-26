from PySide6.QtCore import QObject, Signal


class JarvisEvents(QObject):
    """
    Global J.A.R.V.I.S Event Bus

    Every module communicates through this object.
    """


    # =========================
    # AI EVENTS
    # =========================

    state_changed = Signal(str)

    response_token = Signal(str)

    response_finished = Signal(str)

    ai_request = Signal(str)

    ai_error = Signal(str)


    # =========================
    # VOICE EVENTS
    # =========================

    wake_word_detected = Signal()

    voice_command = Signal(str)

    microphone_started = Signal()

    microphone_stopped = Signal()


    # =========================
    # SYSTEM EVENTS
    # =========================

    system_updated = Signal(dict)

    cpu_changed = Signal(float)

    ram_changed = Signal(float)

    disk_changed = Signal(float)

    network_changed = Signal(dict)

    battery_changed = Signal(object)

    # =========================
    # UI EVENTS
    # =========================

    notification = Signal(str)

    page_changed = Signal(str)

    hud_message = Signal(str)


    # =========================
    # MEMORY EVENTS
    # =========================

    memory_added = Signal(str)

    memory_recalled = Signal(str)


    # =========================
    # AUTOMATION EVENTS
    # =========================

    open_application = Signal(str)

    close_application = Signal(str)


    # =========================
    # ANDROID EVENTS
    # =========================

    android_connected = Signal()

    android_disconnected = Signal()


    # =========================
    # DEBUG EVENTS
    # =========================

    log = Signal(str)

    warning = Signal(str)

    error = Signal(str)



jarvis_events = JarvisEvents()