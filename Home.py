import time
import streamlit as st
import datetime

st.set_page_config(layout="wide")


def fastenzeit(startzeit):
    jetzt = datetime.datetime.now()
    delta = jetzt - startzeit
    tage = delta.days
    stunden, rest = divmod(delta.seconds, 3600)
    minuten, sekunden = divmod(rest, 60)
    st.write(
        "Du fastest seit {} Tagen, {} Stunden, {} Minuten und {} Sekunden".format(tage, stunden, minuten, sekunden))
    gesamtsekunden = delta.total_seconds()
    progress = min(gesamtsekunden / (7 * 24 * 60 * 60), 1.0)
    progress_bar(progress)


def progress_bar(progress):
    red = 255
    green = 0
    blue = 0

    if progress <= 0.5:
        green = int(510 * progress)
    else:
        red = int(510 * (1 - progress))
        green = 255

    progress_percentage = progress * 100
    bar_style = f"""
    <style>
    .progress {{
        background-color: #f3f3f3;
        width: 100%;
        height: 30px;
        display: flex;
    }}
    .progress-value {{
        width: {progress_percentage}%;
        height: 100%;
        background-color: rgb({red}, {green}, {blue});
        transition: background-color 1s;
    }}
    </style>
    <div class="progress">
        <div class="progress-value"></div>
    </div>
    """
    st.write(bar_style, unsafe_allow_html=True)


def main():
    st.title("Fastenzeitrechner")
    startzeit = datetime.datetime(2023, 11, 9, 14, 0, 0)
    while True:
        fastenzeit(startzeit)
        time.sleep(1)
        st.experimental_rerun()


if __name__ == "__main__":
    main()
