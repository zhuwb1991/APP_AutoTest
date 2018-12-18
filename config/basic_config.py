import os


PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)


cpu_path = PATH("../report/performance/cpu.txt")
fps_path = PATH("../report/performance/fps.txt")
mem_path = PATH("../report/performance/memory.txt")

performance_path = PATH("../report/性能报告.html")
