from fastai.vision.all import *
from PIL import Image
from torchvision import transforms
import pathlib

temp = pathlib.PosixPath
pathlib.WindowsPath = pathlib.PosixPath


def is_carpet(img):
    model = load_learner('./model_carpet.pkl', cpu=True)
    #model.load(fast_ai_params.weights)
    img = Image.open(img)
    transform = transforms.Compose([
        transforms.PILToTensor()
    ])
    img = transform(img).permute(1, 2, 0)

    is_carpet_wall,_,probs = model.predict(img)
    print(is_carpet_wall, probs)
    return is_carpet_wall, probs[1]



def is_leopard(img):
    model = load_learner('./model_leopard.pkl')
    img = Image.open(img)
    transform = transforms.Compose([
        transforms.PILToTensor()
    ])
    img = transform(img).permute(1, 2, 0)

    is_leopard,_,probs = model.predict(img)
    print(is_leopard, probs)
    return is_leopard


def is_scand(img):
    model = load_learner('model_scandy.pkl')
    img = Image.open(img)
    transform = transforms.Compose([
        transforms.PILToTensor()
    ])
    img = transform(img).permute(1, 2, 0)

    is_scandy,_,probs = model.predict(img)
    print(is_scandy, probs)
    return is_scandy

if __name__ == "__main__":
    is_scandi=True
    is_carpet_wall=True