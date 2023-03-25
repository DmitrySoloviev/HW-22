# В данном коде все прокомментировано как надо,
# но слишком избыточно.
# Избавьтесь от комментариев, изменив имена переменных, 
# чтобы было понятно, за что эти переменные отвечают 
# и что происходит и без комментариев


class Unit:

    def move_unit(self, field, x: int, y: int, direction: str,
                  flying: bool, crawl: bool, points_per_action=1):
        if flying and crawl:
            raise ValueError('Рожденный ползать летать не должен!')

        if flying:
            points_per_action *= 1.2
            if direction == 'UP':
                new_y = y + points_per_action
                new_x = x
            elif direction == 'DOWN':
                new_y = y - points_per_action
                new_x = x
            elif direction == 'LEFT':
                new_y = y
                new_x = x - points_per_action
            elif direction == 'RIGHT':
                new_y = y
                new_x = x + points_per_action
        if crawl:
            points_per_action *= 0.5
            if direction == 'UP':
                new_y = y + points_per_action
                new_x = x
            elif direction == 'DOWN':
                new_y = y - points_per_action
                new_x = x
            elif direction == 'LEFT':
                new_y = y
                new_x = x - points_per_action
            elif direction == 'RIGHT':
                new_y = y
                new_x = x + points_per_action

            field.set_unit(x=new_x, y=new_y, unit=self)

#     ...
