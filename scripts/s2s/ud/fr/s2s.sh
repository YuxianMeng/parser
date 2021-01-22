
export PYTHONPATH="$PWD"
export TOKENIZERS_PARALLELISM=false

DATA_DIR="/userhome/yuxian/data/parser/ud-treebanks/ud-treebanks-v2.2/UD_French-GSD"
DATA_PREFIX="fr_gsd-ud-"
BERT_DIR="/userhome/yuxian/data/bert/xlm-roberta-large/"
BERT_TYPE="roberta"

# hyper-params
DROPOUT=0.3
accumulate=150
WARMUP=100
addition=1
LR=4e-5

# save directory
OUTPUT_DIR="/userhome/yuxian/train_logs/dependency/ud-fr/s2s/lr${LR}_accumulate${accumulate}_warmup${WARMUP}_add${addition}"
mkdir -p $OUTPUT_DIR

python parser/s2s_query_trainer.py \
--precision 16 \
--default_root_dir $OUTPUT_DIR \
--data_dir $DATA_DIR --data_prefix $DATA_PREFIX \
--data_format 'conllu' \
--pos_dim 100 \
--bert_dir $BERT_DIR --bert_name $BERT_TYPE \
--additional_layer_dim 1024 \
--additional_layer $addition --additional_layer_type "transformer" \
--mrc_dropout $DROPOUT \
--workers 24 \
--gpus="0,1,2,3" \
--accelerator "ddp" \
--batch_size 4 \
--accumulate_grad_batches $accumulate \
--lr $LR \
--gradient_clip_val=1.0 \
--ignore_punct --predict_child \
--max_epochs 10 \
--group_sample \
--scheduler "linear_decay" --warmup_steps $WARMUP --final_div_factor 20
d