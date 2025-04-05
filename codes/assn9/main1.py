import heapq

class Task:
    def __init__(self, name, duration, dependencies=None):
        self.name = name
        self.duration = duration
        self.dependencies = dependencies if dependencies else []

class TaskScheduler:
    def __init__(self, tasks):
        self.tasks = {task.name: task for task in tasks}
        self.start_times = {}

    def get_heuristic(self, remaining_tasks):
        return sum(task.duration for task in remaining_tasks)

    def a_star_schedule(self):
        open_set = [(0, [])] 
        best_time = float('inf')
        best_schedule = []
        
        while open_set:
            current_time, scheduled = heapq.heappop(open_set)
            remaining = [task for task in self.tasks.values() if task.name not in scheduled]
            
            if not remaining:
                if current_time < best_time:
                    best_time = current_time
                    best_schedule = scheduled
                continue
            
            for task in remaining:
                if all(dep in scheduled for dep in task.dependencies):
                    new_time = current_time + task.duration
                    heapq.heappush(open_set, (new_time + self.get_heuristic(remaining), scheduled + [task.name]))
        
        return best_time, best_schedule
    
    def greedy_schedule(self):
        scheduled = set()
        total_time = 0
        schedule_order = []
        tasks_sorted = sorted(self.tasks.values(), key=lambda x: x.duration)
        
        while tasks_sorted:
            for task in tasks_sorted:
                if all(dep in scheduled for dep in task.dependencies):
                    scheduled.add(task.name)
                    schedule_order.append(task.name)
                    total_time += task.duration
                    tasks_sorted.remove(task)
                    break
        
        return total_time, schedule_order

if __name__ == "__main__":
    tasks = [
        Task("A", 3, []),
        Task("B", 2, ["A"]),
        Task("C", 1, ["A"]),
        Task("D", 4, ["B", "C"]),
        Task("E", 2, ["D"])
    ]
    
    scheduler = TaskScheduler(tasks)
    a_star_result = scheduler.a_star_schedule()
    greedy_result = scheduler.greedy_schedule()
    
    print("A* Search Scheduling:", a_star_result)
    print("Greedy Algorithm Scheduling:", greedy_result)