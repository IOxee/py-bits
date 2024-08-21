interface WorkDayInfo {
    requiredWorkHours: number;
    startTime: string;
    lunchStart: string;
    lunchEnd: string;
    remainingTime: number;
  }
  
  const timeToDecimal = (time: string): number => {
    const [hour, minute] = time.split(':').map(Number);
    return hour + minute / 60;
  };
  
  const decimalToTime = (decimalTime: number): string => {
    const hour = Math.floor(decimalTime);
    const minute = Math.round((decimalTime - hour) * 60);
    return `${hour}:${minute.toString().padStart(2, '0')}`;
  };
  
  const calculateExitTime = (workDayInfo: WorkDayInfo): string => {
    const {requiredWorkHours, startTime, lunchStart, lunchEnd, remainingTime} = workDayInfo;
    
    const startTimeDecimal = timeToDecimal(startTime);
    const lunchStartDecimal = timeToDecimal(lunchStart);
    const lunchEndDecimal = timeToDecimal(lunchEnd);
    const morningWorkHours = lunchStartDecimal - startTimeDecimal;
    const lunchDuration = lunchEndDecimal - lunchStartDecimal;
    const afternoonWorkHours = requiredWorkHours - morningWorkHours + remainingTime;
  
    const exitTimeDecimal = lunchEndDecimal + afternoonWorkHours;
    return decimalToTime(exitTimeDecimal);
  };
  
  const calculateLunchDuration = (workDayInfo: WorkDayInfo): string => {
    const lunchStartDecimal = timeToDecimal(workDayInfo.lunchStart);
    const lunchEndDecimal = timeToDecimal(workDayInfo.lunchEnd);
    const lunchDuration = lunchEndDecimal - lunchStartDecimal;
    return decimalToTime(lunchDuration);
  };
  
  const calculateDaytimeDuration = (workDayInfo: WorkDayInfo): string => {
    const startTimeDecimal = timeToDecimal(workDayInfo.startTime);
    const lunchStartDecimal = timeToDecimal(workDayInfo.lunchStart);
    return decimalToTime(lunchStartDecimal - startTimeDecimal);
  };
  
  const workDayInfo: WorkDayInfo = {
    requiredWorkHours: timeToDecimal("6:30"),
    startTime: "08:11",
    lunchStart: "14:30",
    lunchEnd: "14:30",
    remainingTime: timeToDecimal("00:00")
  };
  
  const exitTime = calculateExitTime(workDayInfo);
  
  const morningStartTime = workDayInfo.startTime;
  const lunchStartTime = workDayInfo.lunchStart;
  
  const morningStartTimeDecimal = timeToDecimal(morningStartTime);
  const lunchStartTimeDecimal = timeToDecimal(lunchStartTime);
  
  const morningWork = lunchStartTimeDecimal - morningStartTimeDecimal;
  const workedOnDay = calculateDaytimeDuration(workDayInfo);
  const remainingWork = workDayInfo.requiredWorkHours - morningWork;
  const remainingWorkPlusExtraTime = workDayInfo.remainingTime >= 0.01 ? remainingWork + workDayInfo.remainingTime : 0;
  console.clear();
  console.log(
    "\n" +
    "------------------------------------------------------\n" +
    "|                  Summary of the day                |\n" +
    "------------------------------------------------------\n" +
    `| In the morning you have worked: ${workedOnDay.padEnd(21, ' ')} |\n` +
    `| You have eaten during ${calculateLunchDuration(workDayInfo)} minutes${"".padEnd(23 - calculateLunchDuration(workDayInfo).length, ' ')} |\n` +
    `| You are missing ${decimalToTime(remainingWork)} hours to finish ${"".padEnd(16, ' ')}|\n` +
    `| You must do ${decimalToTime(workDayInfo.remainingTime)} of extra time ${"".padEnd(15, ' ')}|\n` +
    `| Your departure time would be to ${exitTime}${"".padEnd(20 - exitTime.length, ' ')} |\n` +
    `| You should have worked a total of ${decimalToTime(timeToDecimal(workedOnDay) + remainingWork)} hours${"".padEnd(3, ' ')} |\n` +
    "------------------------------------------------------\n"
  );