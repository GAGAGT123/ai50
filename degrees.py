def shortest_path(source, target):
    from util import QueueFrontier
    
    frontier = QueueFrontier()
    frontier.add({"state": source, "path": []})
    explored = set()
    
    while not frontier.empty():
        node = frontier.remove()
        state, path = node["state"], node["path"]
        
        if state == target:
            return path
            
        if state not in explored:
            explored.add(state)
            for movie_id, person_id in neighbors_for_person(state):
                if person_id not in explored and not frontier.contains_state(person_id):
                    new_path = path + [(movie_id, person_id)]
                    if person_id == target:
                        return new_path
                    frontier.add({"state": person_id, "path": new_path})
    
    return None
