import argparse

parser = argparse.ArgumentParser(description='label smoothing experimental feature of the age estimation')

# general parameters
parser.add_argument('--log_dir', type=str, help='log directory')

parser.add_argument('--loading_jobs', type=int, default = 4, help="the number of cpu to load job")
parser.add_argument('--num_workers', type=int, default=4)

parser.add_argument('--weight_decay', type=float, default=1e-6)

parser.add_argument('--dataset', type=str, default="CVPR_16_ChaLearn", help="CVPR_16_ChaLearn")
parser.add_argument('--model', type=str, default="MultiClassificationAlexNet",
                    help="[MultiClassificationAlexNet]")
parser.add_argument('--lr_rate', type=float, default=0.001, help='learning rate (default: 0.001)')

# neural network hyperparamter
parser.add_argument('--lr_schedule', type=float, default=8, help='learning rate schedule')
parser.add_argument('--batch_size', type=int, default=2, metavar='N', help='input batch size for training (default: 32)')

parser.add_argument('--epoch', type=int, help="epoch number, default 1", default=60)

parser.add_argument('--classification_loss', type=str, default ="100_classes", 
                    help="age classification loss type, two options, (100_classes, 20_classes, 10_classes, 5_classes)")
# working machine environment
parser.add_argument('--working_machine', type=str, default="thinkstation", help="[thinkstation, Narvi]")

# [1, 1, 1, 1] => [100_classes, 20_classes, 10_classes, 5_classes]
parser.add_argument('--age_classification_combination', type=list, default=[1, 0, 0, 0],
                    help="100-classes age classification, 20-classes age classification, "
                    "10-classes age classification, 5-classes age classification")

parser.add_argument('--label_smoothing', type=bool, default=True, help="label smoothing technique expermental")

# Init Environment
args = parser.parse_args()

