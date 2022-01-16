import init
import logging

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
initBot = init.Initial()

def main():
    if not initBot.check():
        logging.info("bot not started, check the logs and restart")
        exit()
    logging.info("bot starting...")
    initBot.initBot()
    initBot.addAllCommands()
    initBot.startBot()

if __name__ == "__main__":
    main()
