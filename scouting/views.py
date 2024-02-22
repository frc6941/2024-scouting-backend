from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from scouting import models
from scouting.forms import UploadRecordForm
from scouting.models import Record


def record_dump(record: models.Record):
    return {
        'id': record.id,
        'scouter': record.scouter,
        'matchNumber': record.match_number,
        'robot': record.robot,
        'teamNumber': record.team_number,
        'hpAtAmp': record.hp_at_amp,
        'noShow': record.no_show,
        'mobile': record.mobile,
        'autoAmpScored': record.auto_amp_scored,
        'autoAmpMissed': record.auto_amp_missed,
        'autoSpeakerScored': record.auto_speaker_scored,
        'autoSpeakerMissed': record.auto_speaker_missed,
        'autoFoul': record.auto_foul,
        'coopertition': record.coopertition,
        'teleopAmpScored': record.teleop_amp_scored,
        'teleopAmpMissed': record.teleop_amp_missed,
        'teleopSpeakerScored': record.teleop_speaker_scored,
        'teleopSpeakerMissed': record.teleop_speaker_missed,
        'teleopTrap': record.teleop_trap,
        'teleopFoul': record.teleop_foul,
        'endPosition': record.end_position,
        'harmony': record.harmony,
        'offenseSkill': record.offense_skill,
        'defenseSkill': record.defense_skill,
        'humanPlayerRating': record.human_player_rating,
        'driverRating': record.driver_rating,
        'strategyRating': record.strategy_rating,
        'died': record.died,
        'tippedOver': record.tipped_over,
        'card': record.card,
        'comments': record.comments
    }


@csrf_exempt
def upload_record(request):
    if not request.method == 'POST':
        return JsonResponse({'error': 'request.method'}, status=405)

    form = UploadRecordForm(request.POST)

    if not form.is_valid():
        print(form.errors)
        return JsonResponse({'errors': form.errors}, status=400)

    record = Record.objects.create(
        scouter=form.cleaned_data.get('scouter'),
        match_number=form.cleaned_data.get('matchNumber'),
        robot=form.cleaned_data.get('allianceRobot'),
        team_number=form.cleaned_data.get('teamNumber'),
        hp_at_amp=form.cleaned_data.get('hpAtAmp'),
        no_show=form.cleaned_data.get('robotAbsent'),

        mobile=form.cleaned_data.get('mobile'),
        auto_amp_scored=form.cleaned_data.get('autoAmpScored'),
        auto_amp_missed=form.cleaned_data.get('autoAmpMissed'),
        auto_speaker_scored=form.cleaned_data.get('autoSpeakerScored'),
        auto_speaker_missed=form.cleaned_data.get('autoSpeakerMissed'),
        auto_foul=form.cleaned_data.get('autoFoul'),

        coopertition=form.cleaned_data.get('coopertition'),
        teleop_amp_scored=form.cleaned_data.get('teleopAmpScores'),
        teleop_amp_missed=form.cleaned_data.get('teleopAmpMissed'),
        teleop_speaker_scored=form.cleaned_data.get('teleopSpeakerScore'),
        teleop_speaker_missed=form.cleaned_data.get('teleopSpeakerMissed'),
        teleop_trap=form.cleaned_data.get('teleopTrapScored'),
        teleop_foul=form.cleaned_data.get('teleopFoul'),

        end_position=form.cleaned_data.get('endPosition'),
        harmony=form.cleaned_data.get('harmony'),

        offense_skill=form.cleaned_data.get('offenseSkill'),
        defense_skill=form.cleaned_data.get('defenseSkill'),
        human_player_rating=form.cleaned_data.get('humanPlayerRating'),
        driver_rating=form.cleaned_data.get('driverRating'),
        died=form.cleaned_data.get('died'),
        tipped_over=form.cleaned_data.get('tippedOver'),
        card=form.cleaned_data.get('card'),
        comments=form.cleaned_data.get('comments')
    )
    record.save()
    return JsonResponse(record_dump(record), status=200)


def records_dump(records: [models.Record]):
    return [
        record_dump(record)
        for record in records
    ]


def get_all_records(request):
    if not request.method == 'GET':
        return JsonResponse({'error': 'request.method'}, status=405)

    return JsonResponse(records_dump(Record.objects.all()), status=200, safe=False)


def get_team_records(request, team_number):
    if not request.method == 'GET':
        return JsonResponse({'error': 'request.method'}, status=405)

    records = Record.objects.filter(team_number=team_number)
    if not records.exists():
        return JsonResponse({'error': 'team.not_found'}, status=404)

    return JsonResponse(records_dump(records), safe=False)


def get_teams(request):
    if not request.method == 'GET':
        return JsonResponse({'error': 'request.method'}, status=405)

    return JsonResponse(list(set(Record.objects.values_list('team_number', flat=True))), safe=False)
