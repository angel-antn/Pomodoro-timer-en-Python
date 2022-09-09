CICLES = (1500, 300, 1500, 300, 1500, 300, 1500, 1200)


class Timer:
    def __init__(self):
        self.reps = 0
        self.cicle = CICLES[self.reps]
        self.is_on = True

    def reset(self):
        self.reps = 0
        self.cicle = CICLES[self.reps]
        self.is_on = True

    def change(self):
        if self.reps < 7:
            self.reps += 1
            self.cicle = CICLES[self.reps]
        else:
            self.stop()

    def get_minutes(self):
        minutes = f'{int(self.cicle / 60)}'
        if len(minutes) == 1:
            minutes = f'0{minutes}'
        return minutes

    def get_seconds(self):
        seconds = f"{self.cicle % 60}"
        if len(seconds) == 1:
            seconds = f'0{seconds}'
        return seconds

    def decrease_sec(self):
        self.cicle -= 1

    def stop(self):
        self.is_on = False
