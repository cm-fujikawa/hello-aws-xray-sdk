from aws_xray_sdk.core import patch_all, xray_recorder
from time import sleep

patch_all()
xray_recorder.configure(
    service="Sample App",
    plugins=("ECSPlugin",),
    )

@xray_recorder.capture("test subsegment")
def process():
    print(f"segment_name: {xray_recorder.current_segment().name}")
    print(f"subsegment_name: {xray_recorder.current_subsegment().name}")

    while True:
        subsegment = xray_recorder.current_subsegment()
        subsegment.put_annotation("key", "value")
        print(f"segment aws: {xray_recorder.current_segment().aws}")
        print(f"subsegment aws: {xray_recorder.current_subsegment().aws}")
        sleep(3)


def main():
    xray_recorder.begin_segment("test segment")
    process()
    xray_recorder.end_segment()


if __name__ == '__main__':
    main()
