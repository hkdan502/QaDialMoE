import argparse
import os

def mkdir(path):
    if not os.path.exists(path): #디렉터리 없으면
        os.makedirs(path) #생성

def main():
    mkdir(args.output_dir) #default='./outputs_healthver'
    print(args.train_batch_size)
    args.train_batch_size = args.train_batch_size // args.gradient_accumulation_steps
    print(args.train_batch_size)
    # [?]왜 배치크기를 경사누적횟수로 나눈 정수

if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument("--do_train", action='store_true')
    parser.add_argument("--do_eval", action='store_true')
    parser.add_argument("--do_test", action='store_true')
    
    parser.add_argument("--output_dir", default='./outputs_healthver') #같은 레벨 내(./)

    parser.add_argument("--train_batch_size", default=32) #모델 학습 중 parameter를 업데이트할 때 사용할 데이터 개수
    parser.add_argument('--gradient_accumulation_steps', type=int, default=1)
    #미니 배치를 통해 구해진 gradient를 n-step동안 Global Gradients에 누적시킨 후, 한번에 업데이트하는 방법

    args = parser.parse_args()
    print(args)

    #main()
