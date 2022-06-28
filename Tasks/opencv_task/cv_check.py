import cv2
import numpy
from math import sqrt


def find_circles(raw_image):

    gray = cv2.cvtColor(raw_image, cv2.COLOR_BGR2GRAY)
    gray = cv2.medianBlur(gray, 5)

    w, h, _ = raw_image.shape
    delta_r = w // 22

    for i in range(10, 0, -1):
        min_r = delta_r * i
        max_r = delta_r * (i+1)
        circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 1, 200,
                                   param1=100,
                                   param2=30,
                                   minRadius=min_r,
                                   maxRadius=max_r)

        if circles is not None:
            circles = numpy.uint16(numpy.around(circles))
            for t in circles[0, :]:
                yield tuple(t)


def image_match_template(current_img, pattern_img):
    current_img_arr = cv2.cvtColor(numpy.array(current_img), cv2.COLOR_RGB2BGR555)
    pattern_img_arr = cv2.cvtColor(numpy.array(pattern_img), cv2.COLOR_RGB2BGR555)
    res = cv2.matchTemplate(current_img_arr, pattern_img_arr, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
    size = pattern_img_arr.shape
    closest_area = [max_loc[0], max_loc[1], max_loc[0] + size[1], max_loc[1] + size[0]]
    return max_val, closest_area


if __name__ == "__main__":
    src_file = 'target1.jpg'
    pattern_file = 'success.jpg'

    img_target = cv2.imread(src_file)
    img_pattern = cv2.imread(pattern_file)

    output = img_target.copy()

    max_val, closest_area = image_match_template(img_target, img_pattern)
    if closest_area:
        # координаты центра попадания
        sx, sy = (closest_area[0]+closest_area[2])//2, (closest_area[1]+closest_area[3])//2
        cv2.rectangle(output, closest_area[:2], closest_area[2:], (0, 0, 255), 2)

        shoot_point = 0
        found_flag = False
        for i, c in enumerate(find_circles(img_target)):
            # print(i+1, c)
            center = (c[0], c[1])
            radius = c[2]
            r_success = int(sqrt((c[0]-sx)**2 + (c[1]-sy)**2))
            if r_success >= radius and not found_flag:
                shoot_point = i
                found_flag = True
            # print(f'{i+1}, {c}, {r_success=}')
            cv2.circle(output, center, 1, (255, 255, 0), 2)
            cv2.circle(output, center, radius, (255, 0, 0), 3)
            # cv2.circle(output, center, r_success, (0, 255, 0), 2)

        print(f'Nice shoot, you have {shoot_point} points')
        cv2.imshow('output', output)
        cv2.waitKey(0)
    else:
        print(f'No shoots found')