import requests
import speedtest as st


def get_public_ip() -> str:
    resp = requests.get("https://api.ipify.org?format=json", timeout=5)
    resp.raise_for_status()
    return resp.json()["ip"]


def speed_test() -> tuple:
    test = st.Speedtest(secure=True)

    down_speed = test.download()
    down_speed = round(down_speed / 10**6, 2)

    up_speed = test.upload()
    up_speed = round(up_speed / 10**6, 2)

    ping = test.results.ping

    return down_speed, up_speed, ping


def main() -> None:
    down, up, ping = speed_test()
    print(
        "-" * 100,
        f"Your public IP: {get_public_ip()}",
        f"Download speed in Mbps: {down}",
        f"Upload speed in Mbps: {up}",
        f"Ping: {ping}",
        sep="\n",
    )


if __name__ == "__main__":
    main()
