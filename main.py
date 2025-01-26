from nova.core.engine import NovaEngine

def main():
    engine = NovaEngine()
    try:
        engine.start()
    except KeyboardInterrupt:
        engine.stop()

if __name__ == "__main__":
    main()
