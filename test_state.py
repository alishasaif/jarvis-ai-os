from backend.core.app_state import app_state, AIState


def changed(state):
    print("STATE:", state.value)


app_state.state_changed.connect(changed)

print("Starting test...")

app_state.set_state(AIState.LISTENING)
app_state.set_state(AIState.THINKING)
app_state.set_state(AIState.SPEAKING)
app_state.set_state(AIState.IDLE)

print("Finished.")