import cv2


def extract_frames(video_filename):
    """Extract video frames

    Keyword Arguments:
    @param video_filename: The input video file name
    @type video_filename: str

    @returns: The video frames
    @rtype: list
    """
    # Initializing the video decoder
    vhandler = cv2.VideoCapture(video_filename)

    # Reading frames
    v_frames = []
    while True:
        ret, frame = vhandler.read()
        if ret:
            v_frames.append(frame)
        else:
            break

    # Releasing the video
    vhandler.release()

    return v_frames


def get_match_score(d1, d2):
    """Calculates the match score between two SIFT descriptors

    Keyword Arguments:
    @param d1: The first SIFT descriptor
    @type d1: ndarray
    @param d2:The second SIFT descriptor
    @type d2: ndarray

    @returns: The match score between the two SIFT
        descriptors
    @rtype: float
    """
    bf = cv2.BFMatcher()
    matches = bf.knnMatch(d1, d2, k=2)

    sim = 0
    for m, n in matches:
        if m.distance < 0.75 * n.distance:
            sim += 1

    score = sim / min(d1.shape[0], d2.shape[0])

    return score


def get_unique_frames(images):
    """From a set of images it returns the unique ones.
    Images can be cropped, rotated or at different resolutions.

    Keyword Arguments:
    @param images: The input set of images
    @type images: list

    @returns: The unique images
    @rtype: list
    """
    u_images = []
    prev_d = None

    for i, img in enumerate(images):
        print('Processing frame number: %d' % i)
        sift = cv2.xfeatures2d.SIFT_create()
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        _, des = sift.detectAndCompute(gray, None)

        if prev_d is None:
            u_images.append(img)
        else:
            score = get_match_score(prev_d, des)
            print(score)
            if score <= 0.05:
                u_images.append(img)

        prev_d = des

    return u_images  # 108 correct number
