exp=mhubert_kmeans_mix_unit_cs_only

python scripts/compute_proba_BERT.py $exp/test_cs/correct/dedup_not_converted.txt $exp/prob/test_correct.txt \
                                        $exp/checkpoints/checkpoint_best.pt --dict $exp/bin/dict.txt

python scripts/compute_proba_BERT.py $exp/test_cs/wrong/dedup_not_converted.txt $exp/prob/test_wrong.txt \
                                        $exp/checkpoints/checkpoint_best.pt --dict $exp/bin/dict.txt

cat $exp/prob/test_correct.txt $exp/prob/test_wrong.txt > $exp/prob/test.txt

python scripts/evaluate.py --input $exp/prob/test.txt