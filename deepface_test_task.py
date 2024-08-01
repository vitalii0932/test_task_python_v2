from deepface import DeepFace
import json


# V1
def face_verify(img_1: str, img_2: str) -> str:
    """
    face verify function
    :param img_1: path for image 1
    :param img_2: path for image 2
    :return: verify result in json file
    """

    try:
        result_dict = DeepFace.verify(img1_path=img_1, img2_path=img_2)

        # write verify result to json file
        with open('verify_result.json', 'w') as file:
            json.dump(result_dict, file, indent=4, ensure_ascii=False)

        # analyze the verify dict
        if result_dict.get('verified'):
            return 'It`s all good man!'
        return 'How are you?'

    except Exception as e:
        return str(e)


def face_analyze(img: str):
    """
    face analyze function (age, gender and emotion)
    :param img: path for image with some face
    :return: the json file with age, gender and emotion data
    """
    try:
        result_dict = DeepFace.analyze(img_path=img, actions=['age', 'gender', 'emotion'])

        with open('face_analyze.json', 'w') as file:
            json.dump(result_dict, file, indent=4, ensure_ascii=False)

    except Exception as e:
        return e


def main():
    print(face_verify(img_1='faces/em1.jpg', img_2='faces/em3.jpg'))
    face_analyze(img='faces/snoop.jpg')


if __name__ == '__main__':
    main()