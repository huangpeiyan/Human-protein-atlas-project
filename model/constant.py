import os

main_dir = r'/home/bigdata/Documents/DeepLearningProject/datasets/human-protien-data'
test_dir = os.path.join(main_dir, 'test')
train_dir = os.path.join(main_dir, 'train')
info_img_dir = os.path.join(main_dir, 'config.png')
augm_img_dir = os.path.join(main_dir, 'augment.png')
weight_dir = os.path.join(main_dir, 'weights.hdf5')
submission_csv = os.path.join(main_dir, 'submission.csv')
input_dim = 224
input_channel = 3
batch_size = 128
n_classes = 28
epochs = 50
THRESHOLD = 0.5
