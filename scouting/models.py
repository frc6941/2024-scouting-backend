from django.db import models


class PitTeam(models.Model):
    id = models.BigAutoField(primary_key=True)
    team_number = models.CharField(null=False)
    can_amp = models.BooleanField(null=False)
    can_speaker = models.BooleanField(null=False)
    can_trap = models.BooleanField(null=False)
    chassis_type = models.CharField(max_length=30, null=False)
    cycle_time = models.CharField(max_length=30, null=False)
    auto_type = models.CharField(max_length=30, null=False)


class Record(models.Model):
    class AllianceRobot(models.TextChoices):
        RED_1 = 'Red 1'
        RED_2 = 'Red 2'
        RED_3 = 'Red 3'
        BLUE_1 = 'Blue 1'
        BLUE_2 = 'Blue 2'
        BLUE_3 = 'Blue 3'

    class EndPosition(models.TextChoices):
        NO_CLIMB = '无爬升'
        FAILED_CLIMB = '爬升失败'
        PARKED = '停车'
        STAGE = 'Stage'
        SPOTLIGHT = 'Spotlight'

    class Harmony(models.TextChoices):
        NOT_COMPLETE = '无'
        FIRST_ON_CHAIN = '1 链'
        SECOND_ON_CHAIN = '2 链'
        THIRD_ON_CHAIN = '3 链'

    class Cards(models.TextChoices):
        NO = '无'
        RED_CARD = '红牌'
        YELLOW_CARD = '黄牌'

    id = models.BigAutoField(primary_key=True)
    scouter = models.CharField(max_length=30, null=False)
    match_number = models.CharField(max_length=30, null=False)
    robot = models.CharField(max_length=10, choices=AllianceRobot.choices, null=False)
    team_number = models.IntegerField(null=False)
    hp_at_amp = models.BooleanField(null=False)
    no_show = models.BooleanField(null=False)

    mobile = models.BooleanField(null=False)
    auto_amp_scored = models.IntegerField(null=False)
    auto_amp_missed = models.IntegerField(null=False)
    auto_speaker_scored = models.IntegerField(null=False)
    auto_speaker_missed = models.IntegerField(null=False)
    auto_foul = models.IntegerField(null=False)

    coopertition = models.BooleanField(null=False)
    teleop_amp_scored = models.IntegerField(null=False)
    teleop_amp_missed = models.IntegerField(null=False)
    teleop_speaker_scored = models.IntegerField(null=False)
    teleop_speaker_missed = models.IntegerField(null=False)
    teleop_trap = models.IntegerField(null=False)
    teleop_foul = models.IntegerField(null=False)

    end_position = models.CharField(max_length=10, choices=EndPosition.choices, null=False)
    harmony = models.CharField(max_length=10, choices=Harmony.choices, null=False)

    offense_skill = models.IntegerField(null=False)
    defense_skill = models.IntegerField(null=False)
    human_player_rating = models.IntegerField(null=False)
    driver_rating = models.IntegerField(null=False)
    strategy_rating = models.IntegerField(null=False)
    cycle_time = models.IntegerField(null=False)
    died = models.BooleanField(null=False)
    tipped_over = models.BooleanField(null=False)
    card = models.CharField(max_length=10, choices=Cards.choices, null=False)
    comments = models.TextField()
