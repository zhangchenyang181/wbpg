#微博个性化文本生成
def parse_args():
    	'''
	Parse Seq2seq with attention arguments.
	'''
	parser = argparse.ArgumentParser(description="Run PCGN training.")

	parser.add_argument('--config', nargs='?',
						default='./configs/pcgn_config.yaml',
						help='Configuration file for model specifications')

	return parser.parse_args()