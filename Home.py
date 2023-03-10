import time
import streamlit as st
import datetime


def fastenzeit(startzeit):
    jetzt = datetime.datetime.now()
    delta = jetzt - startzeit
    tage = delta.days
    stunden, rest = divmod(delta.seconds, 3600)
    minuten, sekunden = divmod(rest, 60)
    st.write("Du fastest seit {} Tagen, {} Stunden, {} Minuten und {} Sekunden".format(tage, stunden, minuten, sekunden))
    gesamtsekunden = delta.total_seconds()
    progress = min(gesamtsekunden / (7 * 24 * 60 * 60), 1.0)
    st.progress(progress)


def main():
    st.title("Fastenzeitrechner")
    startzeit = datetime.datetime(2023, 3, 8, 18, 0, 0)
    while True:
        fastenzeit(startzeit)
        time.sleep(1)
        st.experimental_rerun()


if __name__ == "__main__":
    main()
