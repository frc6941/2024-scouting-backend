from django.forms import Form, fields


class UploadRecordForm(Form):
    scouter = fields.CharField(required=False)

    matchNumber = fields.CharField(required=False)

    allianceRobot = fields.CharField(required=False)
    teamNumber = fields.CharField(required=False)
    hpAtAmp = fields.BooleanField(required=False)
    robotAbsent = fields.BooleanField(required=False)

    mobile = fields.BooleanField(required=False)
    autoAmpScored = fields.IntegerField(required=False)
    autoAmpMissed = fields.IntegerField(required=False)
    autoSpeakerScored = fields.IntegerField(required=False)
    autoSpeakerMissed = fields.IntegerField(required=False)
    autoFoul = fields.IntegerField(required=False)

    coopertition = fields.BooleanField(required=False)
    teleopAmpScored = fields.IntegerField(required=False)
    teleopAmpMissed = fields.IntegerField(required=False)
    teleopSpeakerScored = fields.IntegerField(required=False)
    teleopSpeakerMissed = fields.IntegerField(required=False)
    teleopTrapScored = fields.IntegerField(required=False)
    teleopFoul = fields.IntegerField(required=False)

    endPosition = fields.CharField(required=False)
    harmony = fields.CharField(required=False)

    offenseSkill = fields.IntegerField(required=False)
    defenseSkill = fields.IntegerField(required=False)
    humanPlayerRating = fields.IntegerField(required=False)
    driverRating = fields.IntegerField(required=False)
    strategyRating = fields.IntegerField(required=False)
    cycleTime = fields.IntegerField(required=False)
    died = fields.BooleanField(required=False)
    tippedOver = fields.BooleanField(required=False)
    card = fields.CharField(required=False)
    comments = fields.CharField(required=False)


class UploadPitScoutForm(Form):
    teamNumber = fields.CharField(required=False)
    canAmp = fields.BooleanField(required=False)
    canSpeaker = fields.BooleanField(required=False)
    canTrap = fields.BooleanField(required=False)
    chassisType = fields.CharField(required=False)
    cycleTime = fields.CharField(required=False)
    autoType = fields.CharField(required=False)
