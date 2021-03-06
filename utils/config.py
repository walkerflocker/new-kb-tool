import yaml, sys
class ConfigUtil():
    def getConfig(self):
        try:
            with open('config.yaml', 'r') as stream:
                cfg = yaml.safe_load(stream)
                return cfg
        except FileNotFoundError:
            with open('config.yaml', 'w+') as stream:
                cfg = {
                    'months': {},
                    'transactionNameMap': {}
                }
                yaml.dump(cfg, stream)
                return self.getConfig()
        except:
            print('unexpected error loading config, exiting')
            sys.exit()

    def setConfig(self, cfg):
        with open('config.yaml', 'w+') as stream:
            yaml.dump(cfg, stream)