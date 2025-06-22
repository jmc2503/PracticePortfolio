from sprites import *

def increase_alien_speed(self):
    self.player.speed += 1

def increase_bullet_speed(self):
    Ball.speed += 1


alien_speed_one = SkillNode(None, "Speed 1", increase_alien_speed)
bullet_speed_one = SkillNode(alien_speed_one, "Bullet 1", increase_bullet_speed)
bullet_speed_two = SkillNode(bullet_speed_one, "Bullet 2", increase_bullet_speed)
bullet_speed_three = SkillNode(bullet_speed_two, "Bullet 3", increase_bullet_speed)
alien_speed_two = SkillNode(alien_speed_one, "Speed 2", increase_alien_speed)
alien_speed_three = SkillNode(alien_speed_two, "Speed 3", increase_alien_speed)




skill_list = [alien_speed_one, alien_speed_two, alien_speed_three, bullet_speed_one, bullet_speed_two, bullet_speed_three]

alien_speed_three_tree = TreeNode(alien_speed_three, None, None)
bullet_speed_three_tree = TreeNode(bullet_speed_three, None, None)
bullet_speed_two_tree = TreeNode(bullet_speed_two, None, None)
bullet_speed_one_tree = TreeNode(bullet_speed_one, bullet_speed_two_tree, bullet_speed_three_tree)
alien_speed_two_tree = TreeNode(alien_speed_two, alien_speed_three_tree, None)
skill_tree_root = TreeNode(alien_speed_one, alien_speed_two_tree, bullet_speed_one_tree)