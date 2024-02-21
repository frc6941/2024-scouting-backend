from django.forms import Form, fields


class UploadRecordForm(Form):
    scouter = fields.CharField(required=False)

    matchNumber = fields.CharField(required=False)

    allianceRobot = fields.CharField(required=False)
    teamNumber = fields.CharField(required=False)
    hpAtAmp = fields.BooleanField(required=False)
    robotAbsent = fields.BooleanField(required=False)

    mobile = fields.BooleanField(required=False)
    autoAmpScores = fields.IntegerField(required=False)
    autoAmpMissed = fields.IntegerField(required=False)
    autoSpeakerScore = fields.IntegerField(required=False)
    autoSpeakerMissed = fields.IntegerField(required=False)
    autoFoul = fields.IntegerField(required=False)

    coopertition = fields.BooleanField(required=False)
    teleopAmpScores = fields.IntegerField(required=False)
    teleopAmpMissed = fields.IntegerField(required=False)
    teleopSpeakerScore = fields.IntegerField(required=False)
    teleopSpeakerMissed = fields.IntegerField(required=False)
    teleopTrapScored = fields.IntegerField(required=False)
    teleopFoul = fields.IntegerField(required=False)

    endPosition = fields.CharField(required=False)
    harmony = fields.CharField(required=False)

    offenseSkill = fields.CharField(required=False)
    defenseSkill = fields.CharField(required=False)
    died = fields.BooleanField(required=False)
    tippedOver = fields.BooleanField(required=False)
    card = fields.CharField(required=False)
    comments = fields.CharField(required=False)
