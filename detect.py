import image
from tensorflow import keras

model = keras.models.load_model('personal_color_model1.h5')
print('パーソナルカラー診断を行いたい画像のパスを教えて下さい｡')
path=str(input())
face=image.face(path)
predict_image=image.image_create(face)
scores=model.predict(predict_image)[0]

score=0
predict=[]
for j,k in enumerate(scores):
    predict.append(100*k)
    if score<k:
        score=k
        ans=j
    else:
        continue
print('秋タイプの可能性は:',predict[0],'%です')
print('春タイプの可能性は:',predict[1],'%です')
print('夏タイプの可能性は:',predict[2],'%です')
print('冬タイプの可能性は:',predict[3],'%です')
if ans==0:
    print('あなたは秋タイプです')
elif ans==1:
    print('あなたは春タイプです')
elif ans==2:
    print('あなたは夏タイプです')
elif ans==3:
    print('あなたは冬タイプです')