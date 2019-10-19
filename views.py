def visualize(request):
    global students_ids, counts
    if request.method == "post":
        return redirect('/')
    else:
        for p in Student.objects.raw('SELECT id, stud_id FROM NewEntry_student'):
            students_ids.append(p.stud_id)
            c = inout.objects.filter(stud_id=p.stud_id).count()
            counts.append(c)

        plot = figure(title='Bar Graph', x_axis_label='students ids', y_axis_label='frequency', plot_width=1250, plot_height=700)                    
        plot.vbar(x=students_ids, top=counts, width=0.9)
        plot.y_range.start = 0
        script, div = components(plot)
        students_ids = []
        counts = []

        return render(request, "data_vis.html", {'script': script, 'div': div})
