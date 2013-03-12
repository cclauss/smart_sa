from django import template

register = template.Library()


class GetParticipantStatus(template.Node):
    def __init__(self, participant, obj, var_name=None):
        self.participant = template.Variable(participant)
        self.obj = template.Variable(obj)
        self.var_name = var_name

    def render(self, context):
        p = self.participant.resolve(context)
        o = self.obj.resolve(context)
        status = o.get_participant_status(p)
        if self.var_name:
            context[self.var_name] = status
            return ''
        else:
            return status


@register.tag('get_participant_status')
def get_participant_status(parser, token):
    participant = token.split_contents()[1:][0]
    obj = token.split_contents()[1:][1]
    var_name = None
    if len(token.split_contents()[1:]) > 2:
        # handle "as some_var"
        var_name = token.split_contents()[1:][3]
    return GetParticipantStatus(participant, obj, var_name)


class GetRecommendedNextSession(template.Node):
    def __init__(self, participant, var_name=None):
        self.participant = template.Variable(participant)
        self.var_name = var_name

    def render(self, context):
        p = self.participant.resolve(context)
        next_session = p.next_session()
        if self.var_name:
            context[self.var_name] = next_session
            return ''
        else:
            return next_session


@register.tag('get_recommended_next_session')
def get_recommended_next_session(parser, token):
    participant = token.split_contents()[1:][0]
    var_name = None
    if len(token.split_contents()[1:]) > 1:
        # handle "as some_var"
        var_name = token.split_contents()[1:][2]
    return GetRecommendedNextSession(participant, var_name)


class GetRecommendedNextActivity(template.Node):
    def __init__(self, participant, var_name=None):
        self.participant = template.Variable(participant)
        self.var_name = var_name

    def render(self, context):
        p = self.participant.resolve(context)
        next_activity = p.next_activity()
        if self.var_name:
            context[self.var_name] = next_activity
            return ''
        else:
            return next_activity


@register.tag('get_recommended_next_activity')
def get_recommended_next_activity(parser, token):
    participant = token.split_contents()[1:][0]
    var_name = None
    if len(token.split_contents()[1:]) > 1:
        # handle "as some_var"
        var_name = token.split_contents()[1:][2]
    return GetRecommendedNextActivity(participant, var_name)


class ParticipantCompletedAllActivitiesInSession(template.Node):
    def __init__(self, participant, session, var_name=None):
        self.participant = template.Variable(participant)
        self.session = template.Variable(session)
        self.var_name = var_name

    def render(self, context):
        p = self.participant.resolve(context)
        s = self.session.resolve(context)
        status = s.completed_all_activities(p)
        if self.var_name:
            context[self.var_name] = status
            return ''
        else:
            return status


@register.tag('participant_completed_all_activities_in_session')
def participant_completed_all_activities_in_session(parser, token):
    participant = token.split_contents()[1:][0]
    session = token.split_contents()[1:][1]
    var_name = None
    if len(token.split_contents()[1:]) > 2:
        # handle "as some_var"
        var_name = token.split_contents()[1:][3]
    return ParticipantCompletedAllActivitiesInSession(
        participant, session, var_name)


class ParticipantCompletedAllSessionsInIntervention(template.Node):
    def __init__(self, participant, intervention, var_name=None):
        self.participant = template.Variable(participant)
        self.intervention = template.Variable(intervention)
        self.var_name = var_name

    def render(self, context):
        p = self.participant.resolve(context)
        i = self.intervention.resolve(context)
        status = i.completed_all_sessions(p)
        if self.var_name:
            context[self.var_name] = status
            return ''
        else:
            return status


@register.tag('participant_completed_all_sessions_in_intervention')
def participant_completed_all_sessions_in_intervention(parser, token):
    participant = token.split_contents()[1:][0]
    intervention = token.split_contents()[1:][1]
    var_name = None
    if len(token.split_contents()[1:]) > 2:
        # handle "as some_var"
        var_name = token.split_contents()[1:][3]
    return ParticipantCompletedAllSessionsInIntervention(
        participant, intervention, var_name)