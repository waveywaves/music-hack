from scamp import Session, test_run
session = Session(tempo=100)

print(session.print_available_midi_output_devices())

clarinet = session.new_part("clarinet")
clarinet.play_note(60,0.8,10)

