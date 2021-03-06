export PYTHONPATH="$PWD"
export TOKENIZERS_PARALLELISM=false

DATA_DIR="/userhome/yuxian/data/parser/ctb5_parser"
BERT_DIR="/userhome/ganleilei/data/bert/hfl/chinese-bert-wwm-ext"

MRC_DROPOUT=0.3
LR=8e-6
LAYER=0
WARMUP=300

TIME_DIR="`date +%Y%m%d`"

# todo move data_dir
#OUTPUT_DIR="/data/yuxian/train_logs/dependency/ptb/t2t/20210104/finetune_${LAYER}l_bs128_lr${LR}_dropout${MRC_DROPOUT}_bs128"
OUTPUT_DIR="train_logs/dependency/ctb/t2t/${TIME_DIR}/fine_tune/newsep_newfc_wchild_finetune_${LAYER}l_lr${LR}_dropout${MRC_DROPOUT}_bs2560_warmup${WARMUP}_newinit"


python parser/t2t_trainer.py \
--default_root_dir $OUTPUT_DIR \
--data_dir $DATA_DIR \
--data_format 'conllx' \
--pos_dim 100 \
--bert_dir $BERT_DIR \
--additional_layer $LAYER \
--additional_layer_dim 868 \
--mrc_dropout $MRC_DROPOUT \
--workers 12 \
--gpus="0,1,2,3" \
--accelerator 'ddp' \
--precision 16 \
--batch_size 16 \
--accumulate_grad_batches 40 \
--lr $LR \
--gradient_clip_val=1.0 \
--ignore_punct \
--max_epochs 30 \
--group_sample \
--scheduler "linear_decay" --warmup_steps $WARMUP --final_div_factor 10
