import argparse

parser = argparse.ArgumentParser(description='Multi-loss age estimation')

# general parameters
parser.add_argument('--log_dir', type=str, help='log directory')

parser.add_argument('--loading_jobs', type=int, default = 4, help="the number of cpu to load job")
parser.add_argument('--num_workers', type=int, default=4)

parser.add_argument('--weight_decay', type=float, default=1e-6)


parser.add_argument('--dataset', type=str, default="CVPR_16_ChaLearn", help="CVPR_16_ChaLearn, IMDB_WIKI")
parser.add_argument('--model', type=str, default = "Multi_loss_MobileNet_V1",
                     help="[Multi_loss_AlexNet, Multi_loss_MobileNet_V1]")
parser.add_argument('--lr_rate', type=float, default=0.001, help='learning rate (default: 0.001)')

# neural network hyperparamter
parser.add_argument('--lr_schedule', type=float, default=8, help='learning rate schedule')
parser.add_argument('--batch_size', type=int, default=32, metavar='N',help='input batch size for training (default: 32)')
parser.add_argument('--epoch', type=int, help="epoch number, default 1", default=80)

parser.add_argument('--load_IMDB_WIKI_pretrained_model', type=bool, default=False, help="[False, True]")


parser.add_argument('--loss_weights', type=list, default = [1, 0, 0, 0],
                        help="[1,1,1], multi-loss on age estimation, [classification_loss, l1_regression_loss, euclidean_regression_loss, gaussian_loss]")


parser.add_argument('--classification_loss', type=str, default ="100_classes", 
                        help="age classification loss type, two options, (100_classes, 20_classes, 10_classes, 5_classes)")

parser.add_argument('--l1_regression_loss', type=str, default ="0_5_age_rgs", 
                        help="age regression loss option, three options, (0_20_age_rgs, 0_10_age_rgs, 0_5_age_rgs) regression")


parser.add_argument('--euclidean_regression_loss', type=str, default ="euclidean", 
                        help="euclidean age regression loss option")


parser.add_argument('--all_losses', type=list, default =["classification_loss", "l1_regression_loss", "euclidean_regression_loss", "gaussian_loss"], 
                        help="")                        

# working machine environment
parser.add_argument('--working_machine', type=str, default="thinkstation", help="[thinkstation, narvi]")
# parser.add_argument('--store_folder', type=str, default=["", ""], help="["store_folder_in_thinkstation","store_folder_in_narvi"]")

parser.add_argument('--debug', type=bool, default=True, help="[True, False]")
# parser.add_argument('--age_loss_type', type=str, default="5_age_cls_loss", help="[5_age_cls_loss, 10_age_cls_loss, 20_age_cls_loss]")
# parser.add_argument('--no_age_rgs_loss', type=bool, default=True, help="default false")
# parser.add_argument('--age_rgs_loss_weight', type=float, default=0, help="gaussian_loss_weight")


# parser.add_argument('--5_classes_age_loss_type', type=bool, default=False, help="5_classes_age_loss_type")
# parser.add_argument('--10_classes_age_loss_type', type=bool, default=False, help="10_classes_age_loss_type")
# parser.add_argument('--20_classes_age_loss_type', type=bool, default=False, help="[20_classes_age_loss_type")


# parser.add_argument('--age_loss_gaussian', type=str, default="age_loss_gaussian", help="age_loss_gaussian")
# parser.add_argument('--no_age_loss_gaussian', type=bool, default=True, help="default false")
# parser.add_argument('--age_gaussian_loss_weight', type=float, default=0, help="age_gaussian_loss_weight")

parser.add_argument('--description', type=str, default="test model with only usng Gaussian loss", help="")

# test different technique

parser.add_argument('--label_smoothing', type=bool, default=True, help="label smoothing technique")




# Init Environment
args = parser.parse_args()



print("Multitask learning Face Attribute")
