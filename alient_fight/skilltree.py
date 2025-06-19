from sprites import *

def increase_dog_speed(self):
    self.player.speed += 3

def increase_ball_speed(self):
    Ball.speed += 3

def give_shield(self):
    self.player.get_item()


shield_buff = SkillNode(None, "Shield", give_shield)
ball_plus = SkillNode(shield_buff, "Ball+", increase_ball_speed)
dog_speed = SkillNode(shield_buff, "Speed", increase_dog_speed)
new_skill = SkillNode(ball_plus, "New", None)




skill_list = [shield_buff, ball_plus, dog_speed]

new_skill_tree = TreeNode(new_skill, None, None)
ball_plus_tree = TreeNode(ball_plus, new_skill_tree, None)
dog_speed_tree = TreeNode(dog_speed, None, None)
skill_tree_root = TreeNode(shield_buff, dog_speed_tree, ball_plus_tree)