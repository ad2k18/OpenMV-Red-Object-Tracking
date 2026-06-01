import sensor, image, time

# ----------------------------
# Kamera Setup
# ----------------------------
sensor.reset()
sensor.set_pixformat(sensor.RGB565)
sensor.set_framesize(sensor.QVGA)  # 320x240
sensor.skip_frames(time=2000)

sensor.set_auto_gain(False)
sensor.set_auto_whitebal(False)
sensor.set_auto_exposure(False, exposure_us=20000)

clock = time.clock()

# ----------------------------
# ROTER HOLZ-QUADRAT (LAB)
# ----------------------------
# Diese Werte sind bewusst breit für Holz + Uni-Licht
RED_THRESHOLD = (30, 80, 40, 90, 20, 80)

MIN_PIXELS = 800
MIN_AREA   = 800

print("🔴 Red square tracking started")

# ----------------------------
# Main Loop
# ----------------------------
while True:
    clock.tick()
    img = sensor.snapshot()

    blobs = img.find_blobs(
        [RED_THRESHOLD],
        pixels_threshold=MIN_PIXELS,
        area_threshold=MIN_AREA,
        merge=True
    )

    for blob in blobs:
        # Bounding Box
        img.draw_rectangle(blob.rect(), color=(255, 0, 0), thickness=2)

        # Mittelpunkt
        img.draw_cross(blob.cx(), blob.cy(), color=(0, 255, 0))

        # Koordinaten + Größe
        x = blob.x()
        y = blob.y()
        w = blob.w()
        h = blob.h()
        cx = blob.cx()
        cy = blob.cy()

        # Ausgabe (für ROS / Serial)
        print("BOX:", x, y, w, h, "CENTER:", cx, cy)

    # FPS anzeigen
    img.draw_string(5, 5, "FPS: %.1f" % clock.fps(), color=(255,255,255))
