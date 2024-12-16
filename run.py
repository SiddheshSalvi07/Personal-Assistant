def tostartai():
    print("process 1 is running.")
    from main import start
    start()

def tolistenhotword():
    print("process 2 is running.")
    from engine.features import hotWordDetection
    hotWordDetection()


if __name__ == "__main__":  
    import multiprocessing
    p1 = multiprocessing.Process(target=tostartai)
    p2 = multiprocessing.Process(target=tolistenhotword)
    p1.start()
    p2.start()
    p1.join()
    if p2.is_alive():
        p2.terminate()
        p2.join()
    print("Ai terminated")


